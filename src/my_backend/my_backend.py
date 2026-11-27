"""Example module for the demo package"""

import math
import statistics

from .logger_config import logger


def hello_world(message):
    """Example function to say Hello world with a message"""
    logger.debug("This is DEBUG level log message")
    logger.info("This is INFO level log message")
    logger.warning("This is WARN level log message")
    logger.error("This is ERROR level log message")
    return f"Hello world!: {message}"


def descriptive_stats(numbers):
    """Calculate descriptive statistics for numeric data."""
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required.")

    if not all(math.isfinite(x) for x in numbers):
        raise ValueError("All numbers must be finite.")

    return {
        "Count": len(numbers),
        "Mean": statistics.mean(numbers),
        "Median": statistics.median(numbers),
        "Std": statistics.stdev(numbers),
        "Min": min(numbers),
        "Max": max(numbers),
    }
