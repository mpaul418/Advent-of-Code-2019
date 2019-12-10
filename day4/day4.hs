module Day4 where

import Data.Char (digitToInt)

validPassword :: [Int] -> Bool
validPassword x
    | neverDecreasing(x) && twoAdjDigits(x) = True
    | otherwise                             = False

neverDecreasing :: [Int] -> Bool
neverDecreasing (x1:x2:xs)
    | x1 > x2       = False
    | otherwise     = neverDecreasing(x2:xs)
neverDecreasing _   = True

twoAdjDigits :: [Int] -> Bool
twoAdjDigits (x1:x2:xs)
    | x1 == x2  = True
    | otherwise = twoAdjDigits(x2:xs)
twoAdjDigits _  = False

passwordsInRange :: Int -> Int -> Int
passwordsInRange start end
    | start >= end                        = 0
    | validPassword intAsDigits == True   = 1 + passwordsInRange (start + 1) end
    | otherwise                           = passwordsInRange (start + 1) end
    where intAsDigits = map digitToInt (show start)
