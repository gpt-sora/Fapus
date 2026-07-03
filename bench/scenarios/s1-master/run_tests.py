import jobs


def main():
    calls = []

    def fake_fetch(url):
        calls.append(url)
        if len(calls) < 3:
            raise OSError("transient network error")
        return 200

    jobs.fetch_status = fake_fetch
    assert jobs.check("http://example.test/health") is True, "check should survive 2 transient errors"
    print("ALL TESTS PASS")


if __name__ == "__main__":
    main()
