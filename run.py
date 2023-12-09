import sys
import subprocess


def run(day, part, use_example=False):
    day_str = f"day{day}" if day >= 10 else f"day{day}"
    script_path = f"{day_str}/p{part}.py"
    input_file = f"{day_str}/{'example' if use_example else 'input'}.txt"

    with open(input_file, "r") as file:
        subprocess.run(["python", script_path], stdin=file)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python run.py [day] [part] [any third argument for example]")
        sys.exit(1)

    day = int(sys.argv[1])
    part = int(sys.argv[2])
    use_example = len(sys.argv) > 3  # Use example.txt if any third argument is provided
    run(day, part, use_example)
