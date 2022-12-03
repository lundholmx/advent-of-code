(ns advent.core-test
  (:require [clojure.test :refer :all]
            [advent.core :refer :all]))

(deftest group-into-three
  (is (= 3 (count (group [1 2 3 4 5 6 7 8 9])))))

(deftest priority-of-string
  (is (= 16 (priority "vJrwpWtwJgWrhcsFMMfFFhFp"))))
