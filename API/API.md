# API

*An **API** is an application programming interface. It is a set of rules that allow programs to talk to each other. The developer creates the API on the server and allows the client to talk to it.*

* Advantage of API: the API user doesn't get access to the whole dataset or source code and yet they can get all the information they need.

* Terminology: Endpoint, API Access Key, ```?``` Operator, ...

* Python frameworks to build APIs: *Flask*, *Tornado*, *FastAPI* (much more pythonic)

  

#### Rest API

* **REST** determines how the API looks like. It stands for “Representational State Transfer”. It is a set of rules that developers follow when they create their API. One of these rules states that you should be able to get a piece of data (called a resource) when you link to a specific URL.

* A request is made up of 4 things.

  * *<mark>**The endpoint**</mark>/route*, the url you request for

    * Structure: ```root-endpoint/?```

  * - <u>root-endpoint</u>: the starting point of the API you're requesting from.
    - <u>path</u>: determines the resource you're requesting for.
    - <u>query parameters</u>: give you the option to modify your request with key-value pairs, although not technically part of the REST architecture
      - ```?query1=value1&query2=value2```

  * <mark>***The method***</mark>, the type of request you send to the server

    * 5 types: GET, POST, PUT & PATCH, DELETE
    * 4 possible actions: *Create*, *Read*, *Update* and *Delete* (CRUD).

  * - <u>GET</u> (default request method), get a resource from a server, *READ* operation
    - <u>POST</u>, create a new resource on a server, *CREATE* operation
    - <u>PUT & PATCH</u>, update a resource on a server, *UPDATE* operation
    - <u>DELETE</u>, delete a resource from a server, *DELETE* operation
    - You can set the request method in cURL by writing ```-X``` or ```--request```, followed by the request method. 
      - ```curl -X POST https://api.github.com/user/repos```

  * <mark>***The headers***</mark>, provide information to both the client and server

    * A list of valid headers: [HTTP Headers Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

    * - A **request header** is an HTTP header that can be used in an HTTP request to provide information about the request context, so that the sever can tailor the response.

    * Used for many purposes, such as authentication and providing information about the body content

    *  **HTTP Headers are property-value pairs** (separated by a colon).

      * ```Content-Type: application/json``` tells the server to expect JSON content

  * <mark>***The data/body***</mark>, contains information you want to be sent to the server

    * Only used with *POST*, *PUT*, *PATCH* or *DELETE* requests.
    * To send data through cURL, you can use the ```-d``` or``` --data``` option.
    * To send multiple data fields, you can create multiple ```-d``` options.
    * By default, cURL sends data as if they're sent through "form fields" on a page.



* **Testing Endpoints with ```Curl```**
  * In all programming languages, e.g. [Python Requests](https://docs.python-requests.org/en/master/)
  * Command line utility: cURL ([documentation](https://curl.se))

* **Authentication**
  * With a username and password (basic authentication)
  * With a secret token (*oAuth*) - lets you to authenticate yourself with social media networks

* **HTTP Status Codes and Error Messages**
  * 200+ means the request has succeeded.
  * 300+ means the request is redirected to another URL.
  * 400+ means an error that originates from the client has occurred
  * 500+ means an error that originates from the server has occurred

* **API Versions**, you can request for a specific API version in 2 ways

  * - Directly in the endpoint, e.g. Twitter
    - In a request header, e.g. GitHub



__Reference__

[A Layman's Guide for Data Scientists to create APIs in minutes](https://towardsdatascience.com/a-layman-guide-for-data-scientists-to-create-apis-in-minutes-31e6f451cd2f), with hands-on guide to write an API with FastAPI

[Understanding And Using REST APIs](https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/)

[Swagger](https://swagger.io/), API development tool

[RequestBin](https://requestbin.com), a tool to create endpoint and you'll be given a URL that you can use to test requests

[Pipedream](https://pipedream.com/docs/#what-is-pipedream), a production-scale serverless platform to connect APIs, remarkably fast

[Everthing curl](https://everything.curl.dev/), an extensive guide for all things curl
