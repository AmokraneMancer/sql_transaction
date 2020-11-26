
import pyodbc


if __name__ == '__main__':
    conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-0G5VHDF\SQLEXPRESS;Database=WideWorldImporters-Full;Trusted_Connection=yes;')
    req_avant_transaction = "select top 10 StockItemID, StockItemName, UnitPrice, MarketingComments from Warehouse.StockItems"
    try:
        conn.autocommit = False
        cursor = conn.cursor()
        sql_update_price_query = "update Warehouse.StockItems set UnitPrice = '100' where StockItemID=1"
        cursor.execute(sql_update_price_query)
        sql_update_name_query = "update Warehouse.StockItems set StockItemName = 'Clé usb 38' where StockItemID=2"
        cursor.execute(sql_update_name_query)
        sql_update_comment_query = "update Warehouse.StockItems set MarketingComments='Clé usb 100' where StockItemID=5"
        cursor.execute(sql_update_comment_query)
        conn.commit()
        print('commited')
    except Exception:
        conn.rollback()
        print('rollback')
        #Transaction
    finally:
        cursor.execute(req_avant_transaction)
        for r in cursor.fetchall():
            print(r)
        cursor.close()
        conn.close()
        print("connection is closed")

