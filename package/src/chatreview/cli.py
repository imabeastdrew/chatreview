import argparse


def main() -> None:
    parser = argparse.ArgumentParser(prog="chatreview", description="ChatReview CLI")
    parser.add_argument("name", nargs="?", default="World")
    args = parser.parse_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()

