{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "33de42d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "43791bf9",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'pandas' has no attribute 'series'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-1aa6adb8a2b2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mcity1\u001b[0m \u001b[1;33m=\u001b[0m\u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mseries\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m8\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\__init__.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(name)\u001b[0m\n\u001b[0;32m    242\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0m_SparseArray\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    243\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 244\u001b[1;33m     \u001b[1;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mf\"module 'pandas' has no attribute '{name}'\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    245\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    246\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'pandas' has no attribute 'series'"
     ]
    }
   ],
   "source": [
    "city1 =pd.series([12,-6,8,-3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e6491d55",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'pandas' has no attribute 'series'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-b25cb1c925b1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mcity1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mseries\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m8\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\__init__.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(name)\u001b[0m\n\u001b[0;32m    242\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0m_SparseArray\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    243\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 244\u001b[1;33m     \u001b[1;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mf\"module 'pandas' has no attribute '{name}'\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    245\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    246\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'pandas' has no attribute 'series'"
     ]
    }
   ],
   "source": [
    "city1 = pd.series([12,-6,8,-3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bb81a833",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-b25cb1c925b1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mcity1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mseries\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m8\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
   "source": [
    "city1 = pd.series([12,-6,8,-3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0cc6e872",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d2b7061b",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'pandas' has no attribute 'series'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-b25cb1c925b1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mcity1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mseries\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m8\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\__init__.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(name)\u001b[0m\n\u001b[0;32m    242\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0m_SparseArray\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    243\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 244\u001b[1;33m     \u001b[1;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mf\"module 'pandas' has no attribute '{name}'\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    245\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    246\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'pandas' has no attribute 'series'"
     ]
    }
   ],
   "source": [
    "city1 = pd.series([12,-6,8,-3])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c7717a26",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'pandas' has no attribute 'series'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-b25cb1c925b1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mcity1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mseries\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m8\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\__init__.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(name)\u001b[0m\n\u001b[0;32m    242\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0m_SparseArray\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    243\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 244\u001b[1;33m     \u001b[1;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mf\"module 'pandas' has no attribute '{name}'\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    245\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    246\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'pandas' has no attribute 'series'"
     ]
    }
   ],
   "source": [
    "city1 = pd.series([12,-6,8,-3])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ddc9f7a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "city1 = pd.Series([12,-6,8,-3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cac55391",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "Missing parentheses in call to 'print'. Did you mean print(city1)? (<ipython-input-6-60719815e5bb>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-6-60719815e5bb>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    print city1\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m Missing parentheses in call to 'print'. Did you mean print(city1)?\n"
     ]
    }
   ],
   "source": [
    "print city1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e9e10fb2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    12\n",
       "1    -6\n",
       "2     8\n",
       "3    -3\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9827f1fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([12, -6,  8, -3], dtype=int64)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city1.values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4c2ebcdb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RangeIndex(start=0, stop=4, step=1)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city1.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c8358933",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int64')"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city1.dtype\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0e4931e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "city2 =pd.Series([12,-6,8,-3], index =['day1','day2','day3','day4'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "4be469d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "day1    12\n",
       "day2    -6\n",
       "day3     8\n",
       "day4    -3\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "332db464",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2['day3']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5df065a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "day1    12\n",
       "day2    -6\n",
       "dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2[['day1','day2']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "cf7802ac",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'city' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-15-26a76e93cc87>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mcity\u001b[0m\u001b[1;33m>\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'city' is not defined"
     ]
    }
   ],
   "source": [
    "city>4\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "748a8269",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "day1     True\n",
       "day2    False\n",
       "day3     True\n",
       "day4    False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2>4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "2c151a27",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "day1    12\n",
       "day3     8\n",
       "dtype: int64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2[city2>0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e2e8016f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-6"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2.min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "14bded21",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2.max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1964132b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "day3    8\n",
       "dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2[(city2>2)& (city2<9)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7478905a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "day1    15\n",
       "day2    -3\n",
       "day3    11\n",
       "day4     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2+3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "e34d3e6b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "day1    9\n",
       "day2   -9\n",
       "day3    5\n",
       "day4   -6\n",
       "dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2-3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "9ce90e8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "day1    0\n",
       "day2    0\n",
       "day3    2\n",
       "day4    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2%3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "d622a5e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "day1    4.000000\n",
       "day2   -2.000000\n",
       "day3    2.666667\n",
       "day4   -1.000000\n",
       "dtype: float64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2/3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "60c863ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "day1    36\n",
       "day2   -18\n",
       "day3    24\n",
       "day4    -9\n",
       "dtype: int64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2*3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "39a80e12",
   "metadata": {},
   "outputs": [],
   "source": [
    "data ={'KL':25,'TN':26,'AP':34,'KA':24}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "a018b61e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KL    25\n",
       "TN    26\n",
       "AP    34\n",
       "KA    24\n",
       "dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "34b38912",
   "metadata": {},
   "outputs": [],
   "source": [
    "data=pd.Series(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "f8f8e187",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KL    25\n",
       "TN    26\n",
       "AP    34\n",
       "KA    24\n",
       "dtype: int64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f5d46264",
   "metadata": {},
   "outputs": [],
   "source": [
    "States =['TN','AP','KA','KL','DL','NA']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "a7fe63af",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'states' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-31-007ef6e7e2f4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mcity3\u001b[0m\u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSeries\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mstates\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'states' is not defined"
     ]
    }
   ],
   "source": [
    "city3= pd.Series(data,index=states)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "eade1636",
   "metadata": {},
   "outputs": [],
   "source": [
    "city3= pd.Series(data,index=States)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c8764595",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "TN    26.0\n",
       "AP    34.0\n",
       "KA    24.0\n",
       "KL    25.0\n",
       "DL     NaN\n",
       "NA     NaN\n",
       "dtype: float64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "cecef701",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "TN    False\n",
       "AP    False\n",
       "KA    False\n",
       "KL    False\n",
       "DL     True\n",
       "NA     True\n",
       "dtype: bool"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city3.isna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "e33babd0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DL   NaN\n",
       "NA   NaN\n",
       "dtype: float64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city3[city3.isna()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a9a87e5a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "TN    26.0\n",
       "AP    34.0\n",
       "KA    24.0\n",
       "KL    25.0\n",
       "dtype: float64"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city3[city3.notna()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "46376ce9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "TN     True\n",
       "AP     True\n",
       "KA     True\n",
       "KL     True\n",
       "DL    False\n",
       "NA    False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city3.notna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "b7cf2b77",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-38-a44364392d59>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-38-a44364392d59>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    data ={'year':[2000,2001,2002,2003],'states':['KL'.'TN','MP','KA']}\u001b[0m\n\u001b[1;37m                                                       ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "data ={'year':[2000,2001,2002,2003],'states':['KL'.'TN','MP','KA']}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "4606cf18",
   "metadata": {},
   "outputs": [],
   "source": [
    "data ={'year':[2000,2001,2002,2003],'states':['KL','TN','MP','KA'], 'pop':[300,200,203,900]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "d1074cc9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'year': [2000, 2001, 2002, 2003],\n",
       " 'states': ['KL', 'TN', 'MP', 'KA'],\n",
       " 'pop': [300, 200, 203, 900]}"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "737f5542",
   "metadata": {},
   "outputs": [],
   "source": [
    "pop_data = pd.DataFrame(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "5c2817c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>states</th>\n",
       "      <th>pop</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2000</td>\n",
       "      <td>KL</td>\n",
       "      <td>300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2001</td>\n",
       "      <td>TN</td>\n",
       "      <td>200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2002</td>\n",
       "      <td>MP</td>\n",
       "      <td>203</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2003</td>\n",
       "      <td>KA</td>\n",
       "      <td>900</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year states  pop\n",
       "0  2000     KL  300\n",
       "1  2001     TN  200\n",
       "2  2002     MP  203\n",
       "3  2003     KA  900"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_data\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "6e260137",
   "metadata": {},
   "outputs": [],
   "source": [
    "pop_data1= pd.DataFrame(data,columns= ['year','state','pop','income'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "334a1fc0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>state</th>\n",
       "      <th>pop</th>\n",
       "      <th>income</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>300</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2001</td>\n",
       "      <td>NaN</td>\n",
       "      <td>200</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2002</td>\n",
       "      <td>NaN</td>\n",
       "      <td>203</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2003</td>\n",
       "      <td>NaN</td>\n",
       "      <td>900</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year state  pop income\n",
       "0  2000   NaN  300    NaN\n",
       "1  2001   NaN  200    NaN\n",
       "2  2002   NaN  203    NaN\n",
       "3  2003   NaN  900    NaN"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_data1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "d00be1a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "pop_data1= pd.DataFrame(data,columns= ['year','states','pop','income'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "41f95ea5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>states</th>\n",
       "      <th>pop</th>\n",
       "      <th>income</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2000</td>\n",
       "      <td>KL</td>\n",
       "      <td>300</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2001</td>\n",
       "      <td>TN</td>\n",
       "      <td>200</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2002</td>\n",
       "      <td>MP</td>\n",
       "      <td>203</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2003</td>\n",
       "      <td>KA</td>\n",
       "      <td>900</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year states  pop income\n",
       "0  2000     KL  300    NaN\n",
       "1  2001     TN  200    NaN\n",
       "2  2002     MP  203    NaN\n",
       "3  2003     KA  900    NaN"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_data1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "66abf0c7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    300\n",
       "1    200\n",
       "2    203\n",
       "3    900\n",
       "Name: pop, dtype: int64"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_data1['pop']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "b4ce35d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    NaN\n",
       "1    NaN\n",
       "2    NaN\n",
       "3    NaN\n",
       "Name: income, dtype: object"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_data1['income']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "0a205d70",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'income' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-49-08278ce07739>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mpop_data1\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mincome\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2000\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m6000\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m8000\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m9000\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'income' is not defined"
     ]
    }
   ],
   "source": [
    "pop_data1[income]=[2000,6000,8000,9000]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "bcb795b9",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'income' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-50-08278ce07739>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mpop_data1\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mincome\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2000\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m6000\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m8000\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m9000\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'income' is not defined"
     ]
    }
   ],
   "source": [
    "pop_data1[income]=[2000,6000,8000,9000]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "c3ea57c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "pop_data1['income']=[2000,6000,8000,9000]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "e7bbe534",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>states</th>\n",
       "      <th>pop</th>\n",
       "      <th>income</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2000</td>\n",
       "      <td>KL</td>\n",
       "      <td>300</td>\n",
       "      <td>2000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2001</td>\n",
       "      <td>TN</td>\n",
       "      <td>200</td>\n",
       "      <td>6000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2002</td>\n",
       "      <td>MP</td>\n",
       "      <td>203</td>\n",
       "      <td>8000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2003</td>\n",
       "      <td>KA</td>\n",
       "      <td>900</td>\n",
       "      <td>9000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year states  pop  income\n",
       "0  2000     KL  300    2000\n",
       "1  2001     TN  200    6000\n",
       "2  2002     MP  203    8000\n",
       "3  2003     KA  900    9000"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_data1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "903611f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "pop_data1['debt']=[200,600,800,900]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "bdab6af3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>states</th>\n",
       "      <th>pop</th>\n",
       "      <th>income</th>\n",
       "      <th>debt</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2000</td>\n",
       "      <td>KL</td>\n",
       "      <td>300</td>\n",
       "      <td>2000</td>\n",
       "      <td>200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2001</td>\n",
       "      <td>TN</td>\n",
       "      <td>200</td>\n",
       "      <td>6000</td>\n",
       "      <td>600</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2002</td>\n",
       "      <td>MP</td>\n",
       "      <td>203</td>\n",
       "      <td>8000</td>\n",
       "      <td>800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2003</td>\n",
       "      <td>KA</td>\n",
       "      <td>900</td>\n",
       "      <td>9000</td>\n",
       "      <td>900</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year states  pop  income  debt\n",
       "0  2000     KL  300    2000   200\n",
       "1  2001     TN  200    6000   600\n",
       "2  2002     MP  203    8000   800\n",
       "3  2003     KA  900    9000   900"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_data1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "99a4f06d",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-55-d49846c1a5e4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mpop_data1\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'save'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'income'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'debt'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
     ]
    }
   ],
   "source": [
    "pop_data1['save']=['income']-['debt']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "aaf7a821",
   "metadata": {},
   "outputs": [],
   "source": [
    "pop_data1['save']=pop_data1['income']-pop_data1['debt']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "81bba483",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>states</th>\n",
       "      <th>pop</th>\n",
       "      <th>income</th>\n",
       "      <th>debt</th>\n",
       "      <th>save</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2000</td>\n",
       "      <td>KL</td>\n",
       "      <td>300</td>\n",
       "      <td>2000</td>\n",
       "      <td>200</td>\n",
       "      <td>1800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2001</td>\n",
       "      <td>TN</td>\n",
       "      <td>200</td>\n",
       "      <td>6000</td>\n",
       "      <td>600</td>\n",
       "      <td>5400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2002</td>\n",
       "      <td>MP</td>\n",
       "      <td>203</td>\n",
       "      <td>8000</td>\n",
       "      <td>800</td>\n",
       "      <td>7200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2003</td>\n",
       "      <td>KA</td>\n",
       "      <td>900</td>\n",
       "      <td>9000</td>\n",
       "      <td>900</td>\n",
       "      <td>8100</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year states  pop  income  debt  save\n",
       "0  2000     KL  300    2000   200  1800\n",
       "1  2001     TN  200    6000   600  5400\n",
       "2  2002     MP  203    8000   800  7200\n",
       "3  2003     KA  900    9000   900  8100"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_data1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "f8a02264",
   "metadata": {},
   "outputs": [],
   "source": [
    "del pop_data1['pop']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "9a755265",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>states</th>\n",
       "      <th>income</th>\n",
       "      <th>debt</th>\n",
       "      <th>save</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2000</td>\n",
       "      <td>KL</td>\n",
       "      <td>2000</td>\n",
       "      <td>200</td>\n",
       "      <td>1800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2001</td>\n",
       "      <td>TN</td>\n",
       "      <td>6000</td>\n",
       "      <td>600</td>\n",
       "      <td>5400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2002</td>\n",
       "      <td>MP</td>\n",
       "      <td>8000</td>\n",
       "      <td>800</td>\n",
       "      <td>7200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2003</td>\n",
       "      <td>KA</td>\n",
       "      <td>9000</td>\n",
       "      <td>900</td>\n",
       "      <td>8100</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year states  income  debt  save\n",
       "0  2000     KL    2000   200  1800\n",
       "1  2001     TN    6000   600  5400\n",
       "2  2002     MP    8000   800  7200\n",
       "3  2003     KA    9000   900  8100"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_data1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "a6ed2bef",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'auto_mpg.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-60-51dd789b39f6>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mauto_data\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'auto_mpg.csv'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36mread_csv\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, dialect, error_bad_lines, warn_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options)\u001b[0m\n\u001b[0;32m    608\u001b[0m     \u001b[0mkwds\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkwds_defaults\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    609\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 610\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    611\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    612\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    460\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    461\u001b[0m     \u001b[1;31m# Create the parser.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 462\u001b[1;33m     \u001b[0mparser\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mTextFileReader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    463\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    464\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mchunksize\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0miterator\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[0;32m    817\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"has_index_names\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"has_index_names\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    818\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 819\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engine\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_make_engine\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    820\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    821\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_make_engine\u001b[1;34m(self, engine)\u001b[0m\n\u001b[0;32m   1048\u001b[0m             )\n\u001b[0;32m   1049\u001b[0m         \u001b[1;31m# error: Too many arguments for \"ParserBase\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1050\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mmapping\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# type: ignore[call-arg]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1051\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1052\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_failover_to_python\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, src, **kwds)\u001b[0m\n\u001b[0;32m   1865\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1866\u001b[0m         \u001b[1;31m# open handles\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1867\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_open_handles\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msrc\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1868\u001b[0m         \u001b[1;32massert\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhandles\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1869\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mkey\u001b[0m \u001b[1;32min\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34m\"storage_options\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"encoding\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"memory_map\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"compression\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_open_handles\u001b[1;34m(self, src, kwds)\u001b[0m\n\u001b[0;32m   1360\u001b[0m         \u001b[0mLet\u001b[0m \u001b[0mthe\u001b[0m \u001b[0mreaders\u001b[0m \u001b[0mopen\u001b[0m \u001b[0mIOHanldes\u001b[0m \u001b[0mafter\u001b[0m \u001b[0mthey\u001b[0m \u001b[0mare\u001b[0m \u001b[0mdone\u001b[0m \u001b[1;32mwith\u001b[0m \u001b[0mtheir\u001b[0m \u001b[0mpotential\u001b[0m \u001b[0mraises\u001b[0m\u001b[1;33m.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1361\u001b[0m         \"\"\"\n\u001b[1;32m-> 1362\u001b[1;33m         self.handles = get_handle(\n\u001b[0m\u001b[0;32m   1363\u001b[0m             \u001b[0msrc\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1364\u001b[0m             \u001b[1;34m\"r\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\common.py\u001b[0m in \u001b[0;36mget_handle\u001b[1;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[0;32m    640\u001b[0m                 \u001b[0merrors\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"replace\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    641\u001b[0m             \u001b[1;31m# Encoding\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 642\u001b[1;33m             handle = open(\n\u001b[0m\u001b[0;32m    643\u001b[0m                 \u001b[0mhandle\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    644\u001b[0m                 \u001b[0mioargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'auto_mpg.csv'"
     ]
    }
   ],
   "source": [
    "auto_data=pd.read_csv('auto_mpg.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "5d015481",
   "metadata": {},
   "outputs": [
    {
     "ename": "OSError",
     "evalue": "[Errno 22] Invalid argument: '\"C:\\\\Users\\\\user\\\\AppData\\\\Roaming\\\\jupyter\\\\runtime\\\\auto-mpg.csv\"'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-61-127481259a0e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_csv\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34mr'\"C:\\Users\\user\\AppData\\Roaming\\jupyter\\runtime\\auto-mpg.csv\"'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36mread_csv\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, dialect, error_bad_lines, warn_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options)\u001b[0m\n\u001b[0;32m    608\u001b[0m     \u001b[0mkwds\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkwds_defaults\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    609\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 610\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    611\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    612\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    460\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    461\u001b[0m     \u001b[1;31m# Create the parser.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 462\u001b[1;33m     \u001b[0mparser\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mTextFileReader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    463\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    464\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mchunksize\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0miterator\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[0;32m    817\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"has_index_names\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"has_index_names\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    818\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 819\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engine\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_make_engine\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    820\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    821\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_make_engine\u001b[1;34m(self, engine)\u001b[0m\n\u001b[0;32m   1048\u001b[0m             )\n\u001b[0;32m   1049\u001b[0m         \u001b[1;31m# error: Too many arguments for \"ParserBase\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1050\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mmapping\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# type: ignore[call-arg]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1051\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1052\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_failover_to_python\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, src, **kwds)\u001b[0m\n\u001b[0;32m   1865\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1866\u001b[0m         \u001b[1;31m# open handles\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1867\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_open_handles\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msrc\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1868\u001b[0m         \u001b[1;32massert\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhandles\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1869\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mkey\u001b[0m \u001b[1;32min\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34m\"storage_options\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"encoding\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"memory_map\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"compression\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_open_handles\u001b[1;34m(self, src, kwds)\u001b[0m\n\u001b[0;32m   1360\u001b[0m         \u001b[0mLet\u001b[0m \u001b[0mthe\u001b[0m \u001b[0mreaders\u001b[0m \u001b[0mopen\u001b[0m \u001b[0mIOHanldes\u001b[0m \u001b[0mafter\u001b[0m \u001b[0mthey\u001b[0m \u001b[0mare\u001b[0m \u001b[0mdone\u001b[0m \u001b[1;32mwith\u001b[0m \u001b[0mtheir\u001b[0m \u001b[0mpotential\u001b[0m \u001b[0mraises\u001b[0m\u001b[1;33m.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1361\u001b[0m         \"\"\"\n\u001b[1;32m-> 1362\u001b[1;33m         self.handles = get_handle(\n\u001b[0m\u001b[0;32m   1363\u001b[0m             \u001b[0msrc\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1364\u001b[0m             \u001b[1;34m\"r\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\common.py\u001b[0m in \u001b[0;36mget_handle\u001b[1;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[0;32m    640\u001b[0m                 \u001b[0merrors\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"replace\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    641\u001b[0m             \u001b[1;31m# Encoding\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 642\u001b[1;33m             handle = open(\n\u001b[0m\u001b[0;32m    643\u001b[0m                 \u001b[0mhandle\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    644\u001b[0m                 \u001b[0mioargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mOSError\u001b[0m: [Errno 22] Invalid argument: '\"C:\\\\Users\\\\user\\\\AppData\\\\Roaming\\\\jupyter\\\\runtime\\\\auto-mpg.csv\"'"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv (r'C:\\Users\\user\\AppData\\Roaming\\jupyter\\runtime\\auto-mpg.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "e3a44f02",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv (r'C:\\Users\\user\\AppData\\Roaming\\jupyter\\runtime\\auto-mpg.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "2dd5e8a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>mpg</th>\n",
       "      <th>cylinders</th>\n",
       "      <th>displacement</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>weight</th>\n",
       "      <th>acceleration</th>\n",
       "      <th>model year</th>\n",
       "      <th>origin</th>\n",
       "      <th>car name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>18.0</td>\n",
       "      <td>8</td>\n",
       "      <td>307.0</td>\n",
       "      <td>130</td>\n",
       "      <td>3504</td>\n",
       "      <td>12.0</td>\n",
       "      <td>70</td>\n",
       "      <td>1</td>\n",
       "      <td>chevrolet chevelle malibu</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>15.0</td>\n",
       "      <td>8</td>\n",
       "      <td>350.0</td>\n",
       "      <td>165</td>\n",
       "      <td>3693</td>\n",
       "      <td>11.5</td>\n",
       "      <td>70</td>\n",
       "      <td>1</td>\n",
       "      <td>buick skylark 320</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>18.0</td>\n",
       "      <td>8</td>\n",
       "      <td>318.0</td>\n",
       "      <td>150</td>\n",
       "      <td>3436</td>\n",
       "      <td>11.0</td>\n",
       "      <td>70</td>\n",
       "      <td>1</td>\n",
       "      <td>plymouth satellite</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>16.0</td>\n",
       "      <td>8</td>\n",
       "      <td>304.0</td>\n",
       "      <td>150</td>\n",
       "      <td>3433</td>\n",
       "      <td>12.0</td>\n",
       "      <td>70</td>\n",
       "      <td>1</td>\n",
       "      <td>amc rebel sst</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>17.0</td>\n",
       "      <td>8</td>\n",
       "      <td>302.0</td>\n",
       "      <td>140</td>\n",
       "      <td>3449</td>\n",
       "      <td>10.5</td>\n",
       "      <td>70</td>\n",
       "      <td>1</td>\n",
       "      <td>ford torino</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>393</th>\n",
       "      <td>27.0</td>\n",
       "      <td>4</td>\n",
       "      <td>140.0</td>\n",
       "      <td>86</td>\n",
       "      <td>2790</td>\n",
       "      <td>15.6</td>\n",
       "      <td>82</td>\n",
       "      <td>1</td>\n",
       "      <td>ford mustang gl</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>394</th>\n",
       "      <td>44.0</td>\n",
       "      <td>4</td>\n",
       "      <td>97.0</td>\n",
       "      <td>52</td>\n",
       "      <td>2130</td>\n",
       "      <td>24.6</td>\n",
       "      <td>82</td>\n",
       "      <td>2</td>\n",
       "      <td>vw pickup</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>395</th>\n",
       "      <td>32.0</td>\n",
       "      <td>4</td>\n",
       "      <td>135.0</td>\n",
       "      <td>84</td>\n",
       "      <td>2295</td>\n",
       "      <td>11.6</td>\n",
       "      <td>82</td>\n",
       "      <td>1</td>\n",
       "      <td>dodge rampage</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>396</th>\n",
       "      <td>28.0</td>\n",
       "      <td>4</td>\n",
       "      <td>120.0</td>\n",
       "      <td>79</td>\n",
       "      <td>2625</td>\n",
       "      <td>18.6</td>\n",
       "      <td>82</td>\n",
       "      <td>1</td>\n",
       "      <td>ford ranger</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>397</th>\n",
       "      <td>31.0</td>\n",
       "      <td>4</td>\n",
       "      <td>119.0</td>\n",
       "      <td>82</td>\n",
       "      <td>2720</td>\n",
       "      <td>19.4</td>\n",
       "      <td>82</td>\n",
       "      <td>1</td>\n",
       "      <td>chevy s-10</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>398 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      mpg  cylinders  displacement horsepower  weight  acceleration  \\\n",
       "0    18.0          8         307.0        130    3504          12.0   \n",
       "1    15.0          8         350.0        165    3693          11.5   \n",
       "2    18.0          8         318.0        150    3436          11.0   \n",
       "3    16.0          8         304.0        150    3433          12.0   \n",
       "4    17.0          8         302.0        140    3449          10.5   \n",
       "..    ...        ...           ...        ...     ...           ...   \n",
       "393  27.0          4         140.0         86    2790          15.6   \n",
       "394  44.0          4          97.0         52    2130          24.6   \n",
       "395  32.0          4         135.0         84    2295          11.6   \n",
       "396  28.0          4         120.0         79    2625          18.6   \n",
       "397  31.0          4         119.0         82    2720          19.4   \n",
       "\n",
       "     model year  origin                   car name  \n",
       "0            70       1  chevrolet chevelle malibu  \n",
       "1            70       1          buick skylark 320  \n",
       "2            70       1         plymouth satellite  \n",
       "3            70       1              amc rebel sst  \n",
       "4            70       1                ford torino  \n",
       "..          ...     ...                        ...  \n",
       "393          82       1            ford mustang gl  \n",
       "394          82       2                  vw pickup  \n",
       "395          82       1              dodge rampage  \n",
       "396          82       1                ford ranger  \n",
       "397          82       1                 chevy s-10  \n",
       "\n",
       "[398 rows x 9 columns]"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd625a5d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
