# article text
text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""


def word_frequency(text):

    # convert to lowercase
    text = text.lower()

    # remove punctuation
    text = text.replace(".", "")
    text = text.replace(",", "")

    # split into words
    words = text.split()

    # count word frequency
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    # sort by frequency
    top_words = sorted(
        counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    return top_words


result = word_frequency(text)

print("Top 3 words:")

for word, count in result:
    print(f"{word} - {count} times")