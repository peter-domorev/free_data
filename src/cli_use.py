from main import main

while True:
    try:
        raw_msg = input()

        response = main(raw_msg)
        
        print(response)
    except KeyboardInterrupt:
        break
            
    