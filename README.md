# URL - JSON

# Product: CRUD

### 1. CREATE '/product/create/<name>'

```json
// DATA STYLE
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
	"username": "Coca Cola Company",
	"password": "123456"
}
```

### 2. READ '/product/<hash>'

```json
// DATA STYLE
// NONE
```

### 3. UPDATE '/product/update/<hash>'

```json
// DATA STYLE
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
```

### 4. DELETE '/product/delete/<hash>'

```json
// DATA STYLE
{
	"username": "Coca Cola Company",
	"password": "123456"
}
```

---

---

---

## User: CRUD

### 1. CREATE '/user/create/<username>'

```json
// DATA STYLE
{
	"password": "123456"
}
```

### 2. READ '/user/<username>'

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