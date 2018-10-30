- [grep string after pattern](https://serverfault.com/questions/695310/grep-lines-after-match-until-the-end)
```bash
grep -Pz0 '.*some_pattern(.*\n){#lines_to_return}'
```