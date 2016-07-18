import Test.HUnit
import Data.Char(digitToInt)


toDigits :: Int -> [Int]
toDigits x
  | x > 0 = [ digitToInt x | x <- show x]
  | otherwise = []

toDigitsRev :: Int -> [Int]
toDigitsRev = (reverse . toDigits)

doubleEveryOther :: [Int] -> [Int]
doubleEveryOther = reverse . zipWith (*) (cycle [1, 2]) . reverse

sumDigits :: [Int] -> Int
sumDigits = sum . (map (sum . toDigits))

validate :: Int -> Bool
validate x = ((sumDigits . doubleEveryOther . toDigits) x) `rem` 10 == 0

validateTests = TestList
  [
  TestCase $ assertEqual
    "negative number returns empty list"
    []
    (toDigits 0)
  ,
  TestCase $ assertEqual
    "zero returns empty list"
    []
    (toDigits 0)
  ,
  TestCase $ assertEqual
    "1 returns [1]"
    [1]
    (toDigits 1)
  ,
  TestCase $ assertEqual
    "12 returns [1, 2]"
    [1, 2]
    (toDigits 12)
  ,
  TestCase $ assertEqual
    "negative number returns empty list"
    []
    (toDigitsRev 0)
  ,
  TestCase $ assertEqual
    "zero returns empty list"
    []
    (toDigitsRev 0)
  ,
  TestCase $ assertEqual
    "one number"
    [1]
    (toDigitsRev 1)
  ,
  TestCase $ assertEqual
    "more than one number"
    [2,  1]
    (toDigitsRev 12)
  ,
  TestCase $ assertEqual
    "empty list"
    []
    (doubleEveryOther [])
  ,
  TestCase $ assertEqual
    "doubles second and fourth"
    [2, 1, 2, 1]
    (doubleEveryOther [1, 1, 1, 1])
  , TestCase $ assertEqual
    "doubles only second"
    [1, 2, 1]
    (doubleEveryOther [1, 1, 1])
  , TestCase $ assertEqual
    "doubles only second"
    [1, 2, 1]
    (doubleEveryOther [1, 1, 1])
  , TestCase $ assertEqual
    "sumDigits [] -> 0"
    0
    (sumDigits [])
  , TestCase $ assertEqual
    "sumDigits sums properly"
    2
    (sumDigits [10, 1])
  , TestCase $ assertEqual
    "validate propper number"
    True
    (validate 4012888888881881)
  , TestCase $ assertEqual
    "validate wrong number"
    False
    (validate 4012888888881882)
  ]

--type Peg = String
--type Move = (Peg, Peg)
--aux :: [[Int]] -> [(Int, Int)]
--aux state 
--
----hanoi :: Int-> Peg -> Peg -> Peg -> [Move]
----hanoi x a b c = 
--
--hanoiTests = TestList
--  [
--  TestCase $ assertEqual
--    "can find a solution"
--    [(1, 3), (1, 2), (")]
--    (aux [[1, 2], [], []])
--  --TestCase $ assertEqual
--  --  "can find a solution"
--  --  [("a","c"), ("a","b"), ("c","b")]
--  --  (hanoi 2 "a" "b" "c")
--  ]
main = runTestTT $ TestList [ validateTests ]
