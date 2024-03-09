# Personal application to read books in PDF format

### Getting started

Install dependencies:
1. Festival TTS
2. Ollama + mistral model

Clone this repository.

```
$ git clone https://github.com/jaswdr/pdf_reader
```

Install dependencies with `poetry`.

```
$ poetry install
```

Extract pages.

```
$ poetry shell
$ python -m pdf_reader --pdf ./path/to/file.pdf
```

Start reading it from page 1.

```
$ poetry shell
$ python -m pdf_reader --pdf ./path/to/file.pdf --page 1
```

### Commands

- `<number>`: Got to page <number>
- `<Enter>`: Go to next page
- `r`: Read the page content using Festival TTS
- `s`: Summarize current page (requires Ollama installed with mistral model downloaded)
- `rs`: Read the summary.
