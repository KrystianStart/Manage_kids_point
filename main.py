import group_and_create
import window_main


def main():
    imp = window_main.Main()
    decision = window_main.Main.window(imp)
    match decision:
        case 1:
            group_and_create.Main.window(group_and_create.Main())
        case 2:
            pass


if __name__ == "__main__":
    main()