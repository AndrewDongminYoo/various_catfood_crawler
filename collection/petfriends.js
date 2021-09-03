const fetch = require("node-fetch")
const fs = require("fs")

const obj = {
        table: [],
}

for (let i=1; i<43; i++) {
        let body = {is_express_delivery: false,
                mobile_device_id: "96c9ea0a-f60c-4c89-9280-484f3b616bc3",
                mobile_os_code: "P",
                morning_delivery_possible: false,
                order_by: "product_score",
                page_no: i,
                product_group2_id: 4,
                product_group3_id: null,
                type: "product_group3"}

                fetch("https://mobile.api.pet-friends.co.kr/category/product/list", {
        method: "post",
        body: JSON.stringify(body),
        headers: { "Content-Type": "application/json; charset=UTF-8" }
        })
        .then(res => res.json())
        .then(json => json.data)
        .then(data => data.product_list)
        .then(result => obj.table.push(result))
        .catch(err => console.warn(err))
}

