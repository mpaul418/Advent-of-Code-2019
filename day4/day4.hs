module Day4 where

import Data.Char (digitToInt)

validPassword :: [Int] -> ([Int] -> Bool) -> Bool
validPassword x f
    | neverDecreasing(x) && f x = True
    | otherwise                 = False

neverDecreasing :: [Int] -> Bool
neverDecreasing (x1:x2:xs)
    | x1 > x2       = False
    | otherwise     = neverDecreasing(x2:xs)
neverDecreasing _   = True

twoAdjDigitsP1 :: [Int] -> Bool
twoAdjDigitsP1 (x1:x2:xs)
    | x1 == x2  = True
    | otherwise = twoAdjDigitsP1(x2:xs)
twoAdjDigitsP1 _  = False

twoAdjDigitsP2 :: [Int] -> Bool
twoAdjDigitsP2 (x1:x2:x3:xs)
    | x1 == x2 && x2 /= x3  = True
    | x1 == x2 && x2 == x3  = twoAdjDigitsP2 $ removeDuplicates (xs) x3
    | otherwise             = twoAdjDigitsP2(x2:x3:xs)
twoAdjDigitsP2 (x1:x2:[])
    | x1 == x2              = True
    | otherwise             = False
twoAdjDigitsP2 _            = False

removeDuplicates :: [Int] -> Int -> [Int]
removeDuplicates (x:xs) num
    | x == num          = removeDuplicates xs num
    | otherwise         = (x:xs)
removeDuplicates _ _    = []

passwordsInRange :: Int -> Int -> Int -> Int
passwordsInRange start end 1
    | start >= end                                      = 0
    | validPassword intAsDigits twoAdjDigitsP1 == True  = 1 + passwordsInRange (start + 1) end 1
    | otherwise                                         = passwordsInRange (start + 1) end 1
    where intAsDigits = map digitToInt (show start)
passwordsInRange start end 2
    | start >= end                                      = 0
    | validPassword intAsDigits twoAdjDigitsP2 == True  = 1 + passwordsInRange (start + 1) end 2
    | otherwise                                         = passwordsInRange (start + 1) end 2
    where intAsDigits = map digitToInt (show start)
passwordsInRange _ _ _                                  = 0
