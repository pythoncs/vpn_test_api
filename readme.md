## VPN MongoDB Table Structure

---

### 数据库 Collections 介绍

该项目分为三个collection，分别为userInfos(用户信息)、products(产品信息)、orders(订单信息)

---

#### userInfos

    # session密钥
    sessionKey : String,
    # 用户手机号，作为用户ID
    phone : String,
    # 未失效的验证码
    rightVerificationCode : String,
    # 用户注册时间
    timestamp : String,
    # 用户昵称
    nickname : String,
    # 用户头像
    avatar : String,
    
---

#### products
  
    
    # 用户id
    phone : String,
    # 套餐名称
    packageName : String,
    # 状态  已生效 已过期 即将过期 已失效
    status : String,
    # 价格
    price : Sring,
    # 到期时间
    validUntil : Number,
    # vpn配置信息
    vpn_info : [
      {
        # docker容器ID
        dockerContainerId : String,
        # docker容器名称
        dockerContainerName : String,
        # 产品密码 
        password : String,
        # 产品端口
        port : String,
        # 产品ID
        productId : String,
        # 服务器地址
        server: String,
        # 状态
        status: String,
        # 说明
        text: String,
      }
    ]
    
---

#### orders

    # 用户手机号 用户ID
    phone : String,
    # 付款信息
    payment : [
      {
        # 随机字符串
        nonce_str : String,
        # 创建时间
        create_time : String,
        # 支付金额
        real_fee : Number,
        # 签名
        sign : String,
        # 支付渠道 Alipay|支付宝、Wechat|微信
        channel : String,
        # 渠道方(微信、支付宝等)订单ID
        channel_order_id : String,
        # 订单支付时间，格式为'yyyy-MM-dd HH:mm:ss'，GMT+8
        pay_time : String,
        # 商户订单ID
        partner_order_id : String,
        # 交易时使用的汇率
        rate : String,
        # 订单金额
        total_fee : Number,
        # 币种
        currency : String,
        # UTC时间戳
        time : String,
        # 客户ID
        customer_id : String,
        # GlobePay订单ID
        order_id: String,
      }
    ]
    
目前是大概的一个collection结构，可能后续会增加几个字段

---

