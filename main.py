# Import necessary modules and functions from the website module
from website import create_app, log_server_shutdown, perform_backup_or_restore
import logging, signal, sys

# Check if this script is being run directly
if __name__ == "__main__":
    # Create the Flask application
    app = create_app()

    # Perform backup or restore operation before starting the server
    if not perform_backup_or_restore(app):
        # If backup or restore operation fails, log and exit with non-zero status
        logging.info("Exiting.")
        sys.exit(1)

    # Set up a signal handler for interrupt signals (e.g., Ctrl+C) to gracefully shutdown the server
    signal.signal(signal.SIGINT, lambda signum, frame: log_server_shutdown(signum, frame, app))

    # Log that the server is running
    logging.info("Server is running...")
   
    # Start the Flask application in debug mode
    app.run(debug=True)