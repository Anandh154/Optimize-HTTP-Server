#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    if __name__ == "__main__":
        from django.core.management import execute_from_command_line

        # Check if the port is provided as a command-line argument, default to 8080
        port = sys.argv[2] if len(sys.argv) > 2 else "8080"
        sys.argv = [sys.argv[0], "runserver", f"0.0.0.0:{port}"]

        execute_from_command_line(sys.argv)



if __name__ == '__main__':
    from django.core.management import execute_from_command_line

