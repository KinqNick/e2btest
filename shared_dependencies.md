1. "Flask" - Python micro web framework used in "server.py" to serve the game on a web server. It will also be used to handle requests and responses between "script.js" and "game_logic.py".

2. "Game State" - A data schema that represents the current state of the game. It will be shared between "server.py" and "game_logic.py", and will be sent to "script.js" to update the game in the browser.

3. "SocketIO" - A library used for real-time web communication between the server ("server.py") and the client-side JavaScript ("script.js").

4. "game_logic" - A Python module defined in "game_logic.py" that will be imported and used in "server.py" to handle the game logic.

5. "update_game" - A function defined in "game_logic.py" that will be called in "server.py" to update the game state.

6. "canvas" - An id name of a DOM element in "index.html" that will be used by "script.js" to draw the game.

7. "keydown" - A message name for the event when a key is pressed. It will be used in "script.js" to control the snake and in "server.py" to update the game state.

8. "game_update" - A message name for the event when the game state is updated. It will be used in "server.py" to send the updated game state to "script.js".

9. "draw_game" - A function defined in "script.js" that will be called when the "game_update" event is received to redraw the game.

10. "styles.css" - A CSS file linked in "index.html" that will be used to style the game in the browser.