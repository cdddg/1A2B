# 1A2B

**1A2B**是一種益智[遊戲](https://zh.wikipedia.org/wiki/游戏)，遊戲人數為兩人，或一人與一個人工智慧。



一個人設定一組四碼的[數字](https://zh.wikipedia.org/wiki/数字)作為謎底，另一方猜。每猜一個數，出數者就要根據這個數字給出提示，提示以XAYB形式呈現，直到猜中為止。其中X表示位置正確的數的個數，而Y表示數字正確而位置不對的數的個數。

例如，當謎底為8123，而猜謎者猜1052時，出題者必須提示0A2B。

[猜數字]: https://zh.wikipedia.org/wiki/%E7%8C%9C%E6%95%B0%E5%AD%97



```python
# player solove pc riddle
GameMode().player2pc()

# pc solove pc riddle
GameMode().pc2pc()

# pc solove player riddle
GameMode().pc2player(input('riddle:'))
```


