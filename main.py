from website import create_app, log_server_shutdown, perform_backup_or_restore
import logging, signal, sys

if __name__ == "__main__":
    app = create_app()

    if not perform_backup_or_restore(app):
        logging.info("Exiting.")
        sys.exit(1)

    signal.signal(signal.SIGINT, lambda signum, frame: log_server_shutdown(signum, frame, app))
    logging.info("Server is running...")
    app.run(debug=True)