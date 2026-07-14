from graph import app


def main():
    user_input = input()

    result = app.invoke({"user_input": user_input})
    print(result)


if __name__ == "__main__":
    main()