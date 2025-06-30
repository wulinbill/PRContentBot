import logging, datetime, pathlib, os

def setup_logger(name: str = "prbot") -> logging.Logger:
    log_dir = pathlib.Path("logs") / datetime.date.today().isoformat()
    log_dir.mkdir(parents=True, exist_ok=True)
    logfile = log_dir / "run.log"

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    fh = logging.FileHandler(logfile, encoding="utf-8")
    fh.setFormatter(formatter)

    sh = logging.StreamHandler()
    sh.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(sh)
    return logger