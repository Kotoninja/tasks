package main

import (
	"math/rand"
)

var (
	alphabet string = "abcdefghijklmnopqrstuvwxyz1234567890"
)

type Codec struct {
	db map[string]string
}

func Constructor() *Codec {
	return &Codec{db: map[string]string{}}
}

// Encodes a URL to a shortened URL.
func (this *Codec) encode(longUrl string) string {
	shortUrl := ""
	for i := 0; i < 6; i++ {
		randomIndex := rand.Intn(len(alphabet) - 1)
		shortUrl += string(alphabet[randomIndex])
	}

	this.db[shortUrl] = longUrl

	return shortUrl
}

// Decodes a shortened URL to its original URL.
func (this *Codec) decode(shortUrl string) string {
	return this.db[shortUrl]
}

/**
 * Your Codec object will be instantiated and called as such:
 * obj := Constructor();
 * url := obj.encode(longUrl);
 * ans := obj.decode(url);
 */
