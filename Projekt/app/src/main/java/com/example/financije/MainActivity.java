package com.example.financije;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    private Button shoppingBtn, troskoviBtn, predictionBtn,shoppingList;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initViews();
        shoppingBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, shoppingActivity.class);
                startActivity(intent);
            }
        });
        shoppingList.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, ShoppingListActivity.class);
                startActivity(intent);
            }
        });

        Utils.getInstance();
    }

    private void initViews(){
        shoppingBtn = findViewById(R.id.shoppingBtn);
        predictionBtn = findViewById(R.id.predictionBtn);
        shoppingList = findViewById(R.id.shoppingList);
    }
    public void Family(View view){
        Intent intent = new Intent(MainActivity.this, FamilyActivity.class);
        startActivity(intent);
    }
}

