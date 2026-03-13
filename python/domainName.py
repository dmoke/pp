# Kata: Extract Domain Name
# Parses a URL and extracts the domain name, handling various URL formats including www,
# http/https protocols. Returns just the domain name (e.g., "google" from "https://www.google.com").

def domain_name(url: str):
    if "www" in url:
        return url.split(".")[1]
    if "http" in url:
        return url[8 if url[4] == "s" else 7 : url.find(".")]

    return url.split(".")[0]


def main():
    print(domain_name("https://google.com"))


if __name__ == "__main__":
    main()
