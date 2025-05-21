# my-utils.js Documentation

A lightweight utility library for date formatting, string manipulation, and object utilities.

---

## 📆 Date Utilities

### Function: formatDate(date: Date, format: string): string

Formats a JavaScript `Date` object into a human-readable string using a custom format.

- **Parameters:**
  - `date`: A JavaScript `Date` object.
  - `format`: A format string with tokens like `YYYY`, `MM`, `DD`, `hh`, `mm`, `ss`.

- **Returns:**
  - A formatted string representing the date.

- **Example:**
  ```js
  formatDate(new Date('2023-05-21'), 'YYYY-MM-DD'); // "2023-05-21"
  ```
