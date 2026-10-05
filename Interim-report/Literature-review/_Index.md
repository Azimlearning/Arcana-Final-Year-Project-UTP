---
tags: [moc]
---

# Literature Review — Index

20 sources across 8 domains, sourced from `Interim-report/Docs/02-content.md` §2.1–2.9. Each paper is its own note in this folder with `authors`, `year`, `venue`, `domain`, `gap` frontmatter — filter/sort below instead of scanning prose.

```dataview
TABLE authors, year, venue, gap
FROM "Interim-report/Literature"
WHERE file.name != "_Index"
SORT domain, year ASC
```

## By domain

```dataview
TABLE authors, year
FROM "Interim-report/Literature"
WHERE file.name != "_Index"
GROUP BY domain
```
