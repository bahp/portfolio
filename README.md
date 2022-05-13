## About The Project

This repository contains information about projects I have worked on.

## Getting Started

### Prerequisites

* `jinja`: to create the docs.
* `pyppeteer`: to create the thumbnails.
* `asyncio`: to create the thumbnails.

### Adding a new project

Open the `config.html` file and add a new item...

```sh
    
    name:          # name to show in the card (required)
    url:           # url to link (required)
    thumbnail:     # thumbnail image (optional)
    visible: true  # optional (whether to show or not)
    tags:          # tags (slugs) sperated by space
    s:             # size of the card

```

### Creating docs

Run the following command

```sh
$ python create_jinja.py                # Create html
$ python create_jinja.py --thumbnail    # Create thumbnails and html
```
