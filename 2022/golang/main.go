package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	lines, err := getinput()
	checkErr(err)

	for _, line := range lines {
		fmt.Println(line)
	}
}

func getinput() ([]string, error) {
	if len(os.Args) != 2 {
		fmt.Println("usage: advent <input file>")
		os.Exit(1)
	}

	file, err := os.Open(os.Args[1])
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	lines := []string{}
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines, scanner.Err()
}

func checkErr(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "unexpected error: %s", err)
		os.Exit(1)
	}
}
