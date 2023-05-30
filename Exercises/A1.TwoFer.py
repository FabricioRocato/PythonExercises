def two_fer(name=None):
    if name is None or name.strip() == "":
        name = "you"
    return f"One for {name}, one for me."

def main():
    name = input("Enter a name (leave blank for default): ")
    result = two_fer(name)
    print(result)

if __name__ == "__main__":
    main()
