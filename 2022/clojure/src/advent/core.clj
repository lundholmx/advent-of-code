(ns advent.core
  (:gen-class) 
  (:require
   [clojure.java.io :as io]))

(def names
  ["Harry Potter" "Judithen"])

(def ratings
  {:harry -1 :hermoine 1 :ronald 0})

(defn add+
  "Adds a + to the value passed as argument"
  [s]
  (str s "+"))

(defn multi-arity
  ([]
    (multi-arity "no params"))
  ([a]
  (println "you pass a param:" a)))

(defn varity
  [name & rest]
  (println "Name was" name "and rest:" rest))

(defn group
  ([ls acc curr]
    (if (empty? ls)
      (conj acc curr)
      (let [head (first ls)]
        (if (= head "")
          (group (rest ls) (conj acc curr) 0)
          (group (rest ls) acc (+ (Integer/parseInt (first ls)) curr))
        ))))
  ([ls]
    (group ls [] 0)))

(defn readLines
  [filepath]
  (with-open [reader (io/reader filepath)]
    (reduce conj [] (line-seq reader))))

(defn run
  [infile]
  (println (map add+ names))
  (multi-arity)
  (multi-arity "wow")
  (varity "one" "two" "three")
  (println ratings)
  (let [lines (readLines infile)]
    (println (group lines))))

(defn -main
  ([]
    (println "must provide input file as first argument"))
  ([infile]
    (run infile)))
