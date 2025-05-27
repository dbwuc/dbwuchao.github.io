/**
 * @Author E00687
 * @date 2025/5/22 14:20
 * @Description
 * @Version 1.0
 */
public class EnumSingleClass {
    private enum EnumSingleton{
        INSTANCE;
        private final Singleton realInstance;

        private EnumSingleton(){
            realInstance=new Singleton();
        }



        public Singleton realInstance(){
            return realInstance;
        }


    }

    public static Singleton getInstence(){
        return EnumSingleton.INSTANCE.realInstance;
    }

    public static class Singleton{
        public void doSomething(){
            System.out.println("------------");
        }
    }

//    public static void main(String[] args) {
//        enumSingleton.INSTANCE.doSomething();
//    }
}
