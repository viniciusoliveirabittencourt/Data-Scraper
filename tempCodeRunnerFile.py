  except requests.ReadTimeout:
    print("Your connection has been interrupted.")
    broke = True
    break