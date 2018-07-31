import java.util.*;
class TreeNode{
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode(int x){
		this.left = null;
		this.right = null;
		this.val = x;
	}
	}
public class dcp3{
	
	public static StringBuilder serialize(StringBuilder sb, TreeNode root){
		if (root==null) {
			sb.append("null,");
			return sb;
		}
		sb.append(root.val + ",");
		serialize(sb, root.left);
		serialize(sb, root.right);
		return sb;	
	}
	public static TreeNode deserialize(List<String> data){
		if (data.get(0).equals("null")) return null;
		TreeNode root = new TreeNode(Integer.parseInt(data.get(0)));
		data.remove(0);
		root.left = deserialize(data);
		data.remove(0);
		root.right = deserialize(data);
		return root;
	}
	public static void main(String args[]){
		TreeNode a = new TreeNode(3);
		TreeNode b = new TreeNode(2);
		TreeNode c = new TreeNode(4);
		a.left = b;
		a.right = c;
		StringBuilder sb = new StringBuilder();
		StringBuilder s = serialize(sb, a);
		s.deleteCharAt(s.length()-1);
		String data = s.toString();
		System.out.println(data);
		String[] dataL = data.split(",");
		List<String> list = new LinkedList<>(Arrays.asList(dataL));
		StringBuilder sb1 = new StringBuilder();
		System.out.println(serialize(sb1, deserialize(list)).toString());	
	}
}
