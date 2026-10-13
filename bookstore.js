// Step 2: 
// use bookstore
db = db.getSiblingDB("bookstore")

// Step 3: load authors.json
db.authors.drop()
doc = JSON.parse(fs.readFileSync("authors.json", "utf8"))
db.authors.insertMany(doc)

// Step 4: load books.json
db.books.drop()
doc = JSON.parse(fs.readFileSync("books.json", "utf8"))
db.books.insertMany(doc)

// Step 5: list authors and books
print("Step 5: authors")
printjson(db.authors.find().toArray())
print("Step 5: books")
printjson(db.books.find().toArray())

// Step 6: insert two new books
db.books.insertMany([
  { title: "The Great Gatsby", published_year: 1925, author_ids: ["author_004"] },
  { title: "Game of Thrones", published_year: 1996, author_ids: ["author_005"] }
])

// Step 7: add missing authors
db.authors.insertMany([
  {
    _id: "author_004",
    name: "F. Scott Fitzgerald",
    nationality: "American",
    bio: { short: "American novelist and short story writer.", long: "F. Scott Fitzgerald is best known for The Great Gatsby." }
  },
  {
    _id: "author_005",
    name: "George R. R. Martin",
    nationality: "American",
    bio: { short: "American novelist, short story writer, and essayist.", long: "George R. R. Martin is an American author. He is best known for the series A Song of Ice and Fire." }
  }
])

// Step 8: filter books by a list of authors
print("Step 8: filtered books")
printjson(db.books.find({ author_ids: { $in: ["author_003", "author_004"] } }).toArray())