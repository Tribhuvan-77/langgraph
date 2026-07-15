from graph import app
from uuid import uuid4

def main():
    user_input = input()

    result = app.invoke({"user_input": user_input},config={{"configurable": {"thread_id": uuid4()}}})
    print(result)


if __name__ == "__main__":
    main()