# ---- task 1 ----

def find_min_pledge(pledge_list):
    existing_pledges = set(pledge_list)

    min_pledge = 1
    while min_pledge in existing_pledges:
        min_pledge += 1

    return min_pledge


def test_find_min_pledge():
    assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
    assert find_min_pledge([1, 2, 3]) == 4
    assert find_min_pledge([-1, -3]) == 1
    print("All test cases passed!")


test_find_min_pledge()


# ---- task 2 ----
import feedparser


def get_headlines(rss_url):
    """
    @returns a list of titles from the RSS feed located at `rss_url`
    """
    feed = feedparser.parse(rss_url)

    titles = [entry.title for entry in feed.entries]

    return titles


google_news_url = "https://news.google.com/news/rss"
print(get_headlines(google_news_url))


# ---- task 3 ----
import io

def get_payments_storage():
    """
    Returns an instance of io.BufferedWriter.
    """
    return io.BytesIO()

def stream_payments_to_storage(storage):
    """
    Simulates streaming payments to storage by writing fixed data.
    """
    for i in range(10):
        storage.write(bytes([1, 2, 3, 4, 5]))

class ChecksumStorage(io.BufferedWriter):
    def __init__(self, underlying_storage):
        super().__init__(underlying_storage)
        self.checksum = 0

    def write(self, buffer):
        self.checksum += sum(buffer)
        super().write(buffer)

    def get_checksum(self):
        return self.checksum

def process_payments():
    """
    Processes payments in a streaming fashion by reading from a payment processor
    and writing to a storage system, while also printing a checksum of the bytes written.
    """
    underlying_storage = get_payments_storage()

    checksum_storage = ChecksumStorage(underlying_storage)

    stream_payments_to_storage(checksum_storage)

    print(f"Checksum of bytes written: {checksum_storage.get_checksum()}")


if __name__ == "__main__":
    process_payments()

# ---- task 4 ----
