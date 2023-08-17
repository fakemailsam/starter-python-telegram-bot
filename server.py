import uvicorn
from main2 import app
from main3 import test

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8181)
    test()

