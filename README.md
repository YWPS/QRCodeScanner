# URL - JSON

# Product: CRUD

### 1. CREATE '/product/create/<name>'

```json
// REQUEST
// AUTHENTICATE before request
{
	"code": [
	{
	"name": "Cap",
	"code": 1
	},
	{
	"name": "Bottle",
	"code": 2
	}
	],
	"username": "Coca Cola Company"
}

// RESPONSE
{
   "url": f"https://api.qrserver.com/v1/create-qr-code/?data={id};size=1024*1024"
}
```

### 2. READ '/product/<hash>'

```json
// REQUEST
// NONE
// RESPONSE
{
"name": target.name",
"code": eval(target.code),
"user": target.person.username
}
```

### 3. UPDATE '/product/update/<hash>'

```json
// REQUEST
// AUTHENTICATE USER 
{
    "name": "Coca Cola",
    "code": [
        {
            "name": "Cap",
            "code": 1
        },
        {
            "name": "Bottle",
            "code": 2
        }
    ],
    "username": "Coca Cola Company",
		"password": "123456"
}
// RESPONSE
{
"url": f"https://api.qrserver.com/v1/create-qr-code/?data={id};size=1024*1024"
}
```

### 4. DELETE '/product/delete/<hash>'

```json
// DATA 
{
	"username": "Coca Cola Company",
	"password": "123456
```

---

---

---

# User: CRUD

### 1. CREATE '/user/create/<username>'

```json
// DATA STYLE
{
	"password": "123456"
}
```

### 2. GET '/user/<username>'

```json
// DATA STYLE
// NONE
```

### 3a. UPDATE USERNANE '/user/updateusername'

```json
// DATA STYLE
{
	"oldusername": "Coca Cola",
	"newusername": "Coca Cola Company",
	"password": "123456"
}
```

### 3b. UPDATE PASSWORD '/user/updatepassword'

```json
// DATA STYLE
{
	"username": "Coca Cola",
	"oldpassword": "123456",
	"newpassword": "12345678"
}
```

### 4. DELETE '/user/delete/user'

```json
// DATA STYLE
{
	"password": "123456"
}
```

### 5. AUTH '/auth/username'

```json
// DATA STYLE
{
	"password": "123456"
}
```