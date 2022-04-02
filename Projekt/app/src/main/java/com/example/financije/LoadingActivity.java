package com.example.financije;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;

public class LoadingActivity extends AppCompatActivity {

    boolean isLogedIn=true;//TODO:Nesto bolje od ovog
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading);
        Intent intent;
        if (isLogedIn==false) intent=new Intent(LoadingActivity.this,LoginActivity.class);
        else intent=new Intent(LoadingActivity.this,MainActivity.class);
        startActivity(intent);
    }
}