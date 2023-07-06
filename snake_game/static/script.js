var socket = io.connect('http://' + document.domain + ':' + location.port);
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');

socket.on('connect', function() {
    socket.emit('joined', {});
});

socket.on('status', function(data) {
    $('#chat').val($('#chat').val() + '<' + data.msg + '>\n');
    $('#chat').scrollTop($('#chat').prop('scrollHeight'));
});

socket.on('keydown', function(data) {
    var key = data.key;
    socket.emit('keydown', {key: key});
});

socket.on('game_update', function(data) {
    var game_state = data.game_state;
    draw_game(game_state);
});

function draw_game(game_state) {
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = 'green';
    for (var i = 0; i < game_state.snake.length; i++) {
        var block = game_state.snake[i];
        context.fillRect(block[0], block[1], game_state.block_size, game_state.block_size);
    }
    context.fillStyle = 'red';
    context.fillRect(game_state.food[0], game_state.food[1], game_state.block_size, game_state.block_size);
}

$(document).keydown(function(e) {
    var key = e.which;
    socket.emit('keydown', {key: key});
});