import random

def get_motivational_quote():
    quotes = [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. – Confucius",
        "We may encounter many defeats but we must not be defeated. – Maya Angelou",
        "The secret of getting ahead is getting started. – Mark Twain",
        "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
        "It’s hard to beat a person who never gives up. – Babe Ruth",
        "Everything you’ve ever wanted is on the other side of fear. – George Addair",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis"
    ]
    return random.choice(quotes)

def main():
    print("Here's your motivational quote for the day:")
    print(get_motivational_quote())

if __name__ == "__main__":
    main()