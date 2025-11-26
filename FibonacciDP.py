memo = {} #Creates an empty dictionary
def fib(n): #Defines a function named fib. It'll receive a "n" number
    if n in memo: #Is "n" number written in memo?
        return memo[n] #If yes, it doesn't any calculations just puts the memos answer.

    if n <= 1: #fibonacci start
        return n

    memo[n] = fib(n - 1) + fib(n - 2) #Eğer sayı defterde yoksa ve 1'den büyükse; bir önceki (n-1) ve iki önceki
    # (n-2) sayıları bulmak için kendini tekrar çağırıyor, çıkan sonuçları topluyor ve memo defterine kaydediyor.
    return memo[n] #Deftere kaydettiği o taze sonucu cevap olarak veriyor.

sayi = 3

answer = fib(sayi)
print(f"Answer : {answer}")
