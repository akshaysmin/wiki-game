# wiki-game
find how many clicks from given wikipedia link to philosophy (most are within 20 clicks)

idea from https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy

rules:
1. Clicking on the first non-parenthesized, non-italicized link
2. Ignoring external links, links to the current page, or red links (links to non-existent pages)
3. Stopping when reaching "Philosophy", a page with no links or a page that does not exist, or when a loop occurs
