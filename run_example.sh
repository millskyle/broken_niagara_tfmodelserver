tmux new -d -s example 'echo "Starting server"; bash ./server/run_server.sh; read ' \; split-window -h -d 'echo "Starting client"; python ./client/test.py; read' \; attach\;



