package algorithm;

/**
 * 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
 * 输入：l1 = [1,2,4], l2 = [1,3,4]
 * 输出：[1,1,2,3,4,4]
 * 示例 2：
 * <p>
 * 输入：l1 = [], l2 = []
 * 输出：[]
 * 示例 3：
 * <p>
 * 输入：l1 = [], l2 = [0]
 * 输出：[0]
 */
public class 合并两个有序链表 {
    public Node mergerNode(Node node1, Node node2) {
        if (node1==null)return node1;
        if (node2==null)return node2;
        Node current = new Node(-1);
        while (node1!=null&&node2!=null){
            if (node1.val<node2.val){
                current.next=node1;
                node1.next=node1;
            }else {
                current.next=node2;
                node2.next=node2;
            }
            current=current.next;



        }
//
        current.next=(node1!=null)?node1:node2;

        return node1;
    }
}


class Node {
    int val;
    Node next;

    public Node() {
    }

    public Node(int val) {
        this.val = val;
    }

    public Node(int val, Node next) {
        this.val = val;
        this.next = next;
    }

    public int getVal() {
        return val;
    }

    public void setVal(int val) {
        this.val = val;
    }

    public Node getNext() {
        return next;
    }

    public void setNext(Node next) {
        this.next = next;
    }
}
