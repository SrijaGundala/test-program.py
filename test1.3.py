{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3da42755",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 6\n",
      "The factorial of 6 is 720\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "\n",
    "factorial=1\n",
    "if num < 0:\n",
    "   print( \"no fact exixts:\")\n",
    "elif num == 0:\n",
    "   print(\"The factorial of 0 is 1\")\n",
    "else:\n",
    "   for i in range(1,num + 1):\n",
    "       factorial = factorial*i\n",
    "   print(\"The factorial of\",num,\"is\",factorial)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
