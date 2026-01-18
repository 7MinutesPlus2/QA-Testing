def commission():
    LOCK_PRICE = 45.0
    STOCK_PRICE = 30.0
    BARREL_PRICE = 25.0

    LOCK_LIMIT = 70
    STOCK_LIMIT = 80
    BARREL_LIMIT = 90

    total_locks = 0
    total_stocks = 0 
    total_barrels = 0

    locks = int(input("Locks sold (-1 to finish): "))
    while locks != -1:
        stocks = int(input("Stocks sold: "))
        barrels = int(input("Barrels sold: "))
        total_locks += locks
        total_stocks += stocks
        total_barrels += barrels

        if total_locks > LOCK_LIMIT:
            print("Error: Lock sales exceed monthly limit")
            return
        if total_stocks > STOCK_LIMIT:
            print("Error: Stock sales exceed monthly limit")
            return
        if total_barrels > BARREL_LIMIT:
            print("Error: Barrel sales exceed monthly limit")
            return
            
        locks = int(input("Locks sold (-1 to finish): "))

    if total_locks < 1 or total_stocks < 1 or total_barrels < 1:
        print("Error: Must sell at least one lock, stock, and barrel")
        return

    print(f"Locks sold: {total_locks}")
    print(f"Stocks sold: {total_stocks}")
    print(f"Barrels sold: {total_barrels}")

    lock_sales = LOCK_PRICE * total_locks
    stock_sales = STOCK_PRICE * total_stocks
    barrel_sales = BARREL_PRICE * total_barrels
    sales = lock_sales + stock_sales + barrel_sales
    print(f"Total sales: ${sales:.2f}")

    if sales > 1800.0:
        commission = 0.10 * 1000.0 + 0.15 * 800.0 + 0.20 * (sales - 1800.0)
    elif sales > 1000.0:
        commission = 0.10 * 1000.0 + 0.15 * (sales - 1000.0)
    else:
        commission = 0.10 * sales

    print(f"Commission is ${commission:.2f}")

if __name__ == "__main__":
    commission()