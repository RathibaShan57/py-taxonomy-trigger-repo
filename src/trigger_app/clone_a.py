"""First copy of a duplicated block so jscpd-py reports clone metrics."""


def format_order_summary(order_id: str, items: list[str], paid: bool) -> str:
    header = "ORDER " + order_id
    body = ",".join(items)
    status = "PAID" if paid else "OPEN"
    line_one = header + " " + status
    line_two = "items=" + body
    line_three = "count=" + str(len(items))
    line_four = "ready=" + ("yes" if paid else "no")
    return line_one + "|" + line_two + "|" + line_three + "|" + line_four
