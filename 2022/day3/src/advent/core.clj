(ns advent.core
  (:gen-class) 
  (:require
    [clojure.java.io :as io]
    [clojure.string :as str]
    [clojure.set :as set]))

(def scores "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
(defn score [ch]
  (+ 1 (str/index-of scores ch)))

(defn half
  "Splits line in half"
  [line]
  (let [len (/ (count line) 2)
        a (take len line)
        b (take-last len line)]
    [a b]))

(defn priority [line]
  (let [[a b] (half line)
        common (set/intersection (set a) (set b))
        ch (first common)]
    (score ch)))

(defn group
  "Group list of lines into groups of three."
  ([list groups curr]
    (if (empty? list)
      (conj groups curr)
      (let [head (first list)
            tail (rest list)]
        (case (count curr)
          3 (group tail (conj groups curr) [head])
          (group tail groups (conj curr head))))))
  ([list] (group list [] [])))

(defn group-intersect
  [group]
  (let [[a b c] group
        a (set a)
        b (set b)
        c (set c)]
    (set/intersection a b c)))

(defn readLines
  [filepath]
  (with-open [reader (io/reader filepath)]
    (reduce conj [] (line-seq reader))))

(defn part1
  [lines]
  (let [priorities (map priority lines)]
    (println (reduce + priorities))))

(defn part2
  [lines]
  (let [groups (group lines)
        groups (map group-intersect groups)
        groups (map #(score (first %)) groups)]
    (println (reduce + groups))))

(defn -main
  ([]
    (println "must provide input file as first argument"))
  ([infile]
    (let [lines (readLines infile)]
      (part1 lines)
      (part2 lines))))
